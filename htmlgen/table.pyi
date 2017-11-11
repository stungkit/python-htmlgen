import typing
from typing import Union, AnyStr, List

from htmlgen.element import Element
from htmlgen.generator import Generator


class Table(Element):
    def __init__(self) -> None: ...
    def create_head(self) -> "TableHead": ...
    def create_header_row(self) -> "TableRow": ...
    def create_body(self) -> "TableBody": ...
    def create_row(self) -> "TableRow": ...
    def append_header_row(self, row: "TableRow") -> None: ...
    def append_row(self, row: "TableRow") -> None: ...
    def create_simple_header_row(self, *headers: Union[AnyStr, Generator]) -> "TableRow": ...
    def create_simple_row(self, *cells: Union[AnyStr, Generator]) -> "TableRow": ...
    def generate_header_rows(self) -> typing.Generator["TableRow", None, None]: ...
    def generate_rows(self) -> typing.Generator["TableRow", None, None]: ...

class TableHead(Element):
    def __init__(self) -> None: ...
    def create_row(self) -> "TableRow": ...

class TableBody(Element):
    def __init__(self) -> None: ...
    def create_row(self) -> "TableRow": ...

class TableRow(Element):
    def __init__(self) -> None: ...
    def create_cell(self, content: Union[AnyStr, Generator] = ...) -> "TableCell": ...
    def create_cells(self, *content: Union[AnyStr, Generator]) -> List["TableCell"]: ...
    def create_header_cell(self, content: Union[AnyStr, Generator] = ...) -> "TableHeaderCell": ...
    def create_header_cells(self, *content: Union[AnyStr, Generator]) -> List["TableHeaderCell"]: ...

class TableHeaderCell(Element):
    rows = ...  # type: int
    columns = ...  # type: int
    def __init__(self, *content: Union[AnyStr, Generator]) -> None: ...

class TableCell(Element):
    rows = ...  # type: int
    columns = ...  # type: int
    def __init__(self, *content: Union[AnyStr, Generator]) -> None: ...

class ColumnGroup(Element):
    def __init__(self) -> None: ...
    def create_column(self) -> "Column": ...
    def create_columns_with_classes(self, *css_classes: str) -> List["Column"]: ...

class Column(Element):
    def __init__(self) -> None: ...
