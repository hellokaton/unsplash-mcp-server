# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
from dataclasses import dataclass
from typing import Optional, List, Dict, Union

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
        page: Union[int, str] = 1,
        per_page: Union[int, str] = 10,
        order_by: str = "relevant",
        color: Optional[str] = None,
        orientation: Optional[str] = None
) -> List[UnsplashPhoto]:
    """
    Search for Unsplash photos
    
    Args:
        query: Search keyword
        page: Page number (1-based)
        per_page: Results per page (1-30)
        order_by: Sort method (relevant or latest)
        color: Color filter (black_and_white, black, white, yellow, orange, red, purple, magenta, green, teal, blue)
        orientation: Orientation filter (landscape, portrait, squarish)
    
    Returns:
        List[UnsplashPhoto]: List of search results containing photo objects with the following properties:
            - id: Unique identifier for the photo
            - description: Optional text description of the photo
            - urls: Dictionary of available image URLs in different sizes
            - width: Original image width in pixels
            - height: Original image height in pixels
    """
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    if not access_key:
        raise ValueError("Missing UNSPLASH_ACCESS_KEY environment variable")

    # 确保page是整数类型
    try:
        page_int = int(page)
    except (ValueError, TypeError):
        page_int = 1

    # 确保per_page是整数类型
    try:
        per_page_int = int(per_page)
    except (ValueError, TypeError):
        per_page_int = 10

    params = {
        "query": query,
        "page": page_int,
        "per_page": min(per_page_int, 30),
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
        print(f"HTTP error: {e.response.status_code} - {e.response.text}")
        raise
    except Exception as e:
        print(f"Request error: {str(e)}")
        raise
