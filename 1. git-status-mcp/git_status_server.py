#!/usr/bin/env python3
"""
Git Status MCP Server
A basic MCP server that provides git status information for repositories.
"""


from mcp.server import Server
from mcp.types import Tool

# Initialize the MCP server
app = Server("git-status-mcp")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """All available tools are below."""
    
    return [
        Tool(
            name="git_status",
            description="Get the git status of a repository. Shows modified, staged, and untracked files.",
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Path to the git repository (defaults to current directory if not provided)",
                        "default": "."
                    }
                }
            }
        ),
        Tool(
            name="git_branch",
            description="Get the current branch name and list all branches in the repository.",
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Path to the git repository (defaults to current directory if not provided)",
                        "default": "."
                    }
                }
            }
        ),
        Tool(
            name="git_log",
            description="Get recent commit history (last 10 commits by default).",
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Path to the git repository (defaults to current directory if not provided)",
                        "default": "."
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Number of commits to show (default: 10)",
                        "default": 10,
                        "minimum": 1,
                        "maximum": 100
                    }
                }
            }
        ),
        Tool(
            name="git_diff",
            description="Show changes in the working directory or between commits.",
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Path to the git repository (defaults to current directory if not provided)",
                        "default": "."
                    },
                    "file_path": {
                        "type": "string",
                        "description": "Specific file to show diff for (optional)"
                    }
                }
            }
        )
    ]


