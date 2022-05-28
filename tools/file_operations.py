import glob
from typing import List
import xml.etree.cElementTree as ET


def list_files(file_format: str) -> List:
    files_source = f'./xl_source/*.{file_format}'
    return glob.glob(files_source)


def skip_start_rows(iter_rows: int, number_of_rows_to_skip_at_start: int) -> None:
    for _ in range(number_of_rows_to_skip_at_start):
        next(iter_rows)


def write_tree_to_xml_file(file_path: str, main_test_suite: ET.Element, number_of_current_test_suite: int) -> int:
    tree = ET.ElementTree(main_test_suite)
    file_name = file_path[
        file_path.rfind('\\')+1:file_path.rfind('.xl')
    ]
    tree.write(
        f'xml_results/{file_name}_{number_of_current_test_suite}.xml',
        xml_declaration=True,
        encoding='utf-8')
    number_of_current_test_suite += 1
    return number_of_current_test_suite
