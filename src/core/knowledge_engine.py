"""
Team Obsidian — Distributed AST Knowledge Extraction Engine
Parses multi-language codebases using Tree-sitter, extracts semantic entities,
and constructs high-density dependency graphs for architectural handovers.
"""

import ast
import logging
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)


class AstGraphParser:
    """Extracts classes, functions, and cross-module import dependencies."""

    def __init__(self, language: str = "python"):
        self.language = language
        self.entities: List[Dict[str, Any]] = []
        self.dependencies: List[Dict[str, str]] = []

    def parse_python_module(self, source_code: str, file_path: str) -> Dict[str, Any]:
        """Parse Python source into AST and extract structural symbols."""
        try:
            tree = ast.parse(source_code, filename=file_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    self.entities.append({
                        "name": node.name,
                        "entity_type": "class",
                        "line_start": node.lineno,
                        "docstring": ast.get_docstring(node) or "",
                        "file_path": file_path,
                    })
                elif isinstance(node, ast.FunctionDef):
                    self.entities.append({
                        "name": node.name,
                        "entity_type": "function",
                        "line_start": node.lineno,
                        "docstring": ast.get_docstring(node) or "",
                        "file_path": file_path,
                    })
                elif isinstance(node, (ast.Import, ast.ImportFrom)):
                    mod_name = getattr(node, "module", None) or ", ".join(n.name for n in node.names)
                    self.dependencies.append({
                        "source": file_path,
                        "target": mod_name,
                        "dep_type": "import",
                    })
            return {"entities": self.entities, "dependencies": self.dependencies, "status": "success"}
        except SyntaxError as e:
            logger.error("AST syntax parsing failure in %s: %s", file_path, e)
            return {"entities": [], "dependencies": [], "status": "error", "error": str(e)}


class KnowledgeEntityExtractor:
    """Semantic classifier for architectural components, APIs, and data layers."""

    @staticmethod
    def classify_architecture_tier(file_path: str) -> str:
        if "api" in file_path or "routes" in file_path:
            return "api_gateway"
        if "core" in file_path or "engine" in file_path:
            return "core_business_logic"
        if "services" in file_path or "connectors" in file_path:
            return "external_integration_tier"
        if "models" in file_path or "db" in file_path:
            return "persistence_layer"
        return "general_utility"
