import glob
from typing import List
import xml.etree.cElementTree as ET


def list_files(file_format: str) -> List:
    files_source = f'./xl_source/*.{file_format}'
    return glob.glob(files_source)


def prepare_file_name(file_path: str, number_of_current_test_suite: int) -> str:
    file_name = file_path[
        file_path.rfind('\\')+1:file_path.rfind('.xl')
    ]
    return f'{file_name}_{number_of_current_test_suite}'


def write_tree_to_xml_file(main_element: ET.Element, file_name) -> None:
    tree = ET.ElementTree(main_element)
    tree.write(
        f'xml_results/{file_name}.xml',
        xml_declaration=True,
        encoding='utf-8')
