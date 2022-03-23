from typing import Any

def toBlank(txt: Any, isNone: str = "なし") -> str | Any:
    """もしテキストが`None`なら'なし'などを返す関数です。"""
    if txt is None:
        txt = isNone
    return txt