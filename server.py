# -*- coding: utf-8 -*-

import os
from dataclasses import dataclass
from typing import Optional, List, Dict

import httpx
from dotenv import load_dotenv
from fastmcp import FastMCP

# Load environment variables
load_dotenv()

# Create an MCP server
mcp = FastMCP("Unsplash MCP Server")


@dataclass
class UnsplashPhoto:
    id: str
    description: Optional[str]
    urls: Dict[str, str]
    width: int
    height: int


@mcp.tool()
async def search_photos(
        query: str,
        page: int = 1,
        per_page: int = 10,
        order_by: str = "relevant",
        color: Optional[str] = None,
        orientation: Optional[str] = None
) -> List[UnsplashPhoto]:
    """
    搜索 Unsplash 图片
    
    Args:
        query: 搜索关键词
        page: 页码 (1-based)
        per_page: 每页结果数量 (1-30)
        order_by: 排序方式 (relevant 或 latest)
        color: 颜色过滤 (black_and_white, black, white, yellow, orange, red, purple, magenta, green, teal, blue)
        orientation: 方向过滤 (landscape, portrait, squarish)
    
    Returns:
        List[UnsplashPhoto]: 搜索结果列表
    """
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    if not access_key:
        raise ValueError("Missing UNSPLASH_ACCESS_KEY environment variable")

    params = {
        "query": query,
        "page": page,
        "per_page": min(per_page, 30),
        "order_by": order_by,
    }

    if color:
        params["color"] = color
    if orientation:
        params["orientation"] = orientation

    headers = {
        "Accept-Version": "v1",
        "Authorization": f"Client-ID {access_key}"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.unsplash.com/search/photos",
                params=params,
                headers=headers
            )
            response.raise_for_status()
            data = response.json()

            return [
                UnsplashPhoto(
                    id=photo["id"],
                    description=photo.get("description"),
                    urls=photo["urls"],
                    width=photo["width"],
                    height=photo["height"]
                )
                for photo in data["results"]
            ]
    except httpx.HTTPStatusError as e:
        print(f"HTTP错误: {e.response.status_code} - {e.response.text}")
        raise
    except Exception as e:
        print(f"请求错误: {str(e)}")
        raise
