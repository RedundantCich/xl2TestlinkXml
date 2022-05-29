import glob
from typing import List
import xml.etree.cElementTree as ET


def list_files(file_format: str) -> List:
    files_source = f'./xl_source/*.{file_format}'
    return glob.glob(files_source)


def write_tree_to_xml_file(file_path: str, main_test_suite: ET.Element, number_of_current_test_suite: int) -> None:
    tree = ET.ElementTree(main_test_suite)
    file_name = file_path[
        file_path.rfind('\\')+1:file_path.rfind('.xl')
    ]
    tree.write(
        f'xml_results/{file_name}_{number_of_current_test_suite}.xml',
        xml_declaration=True,
        encoding='utf-8')
