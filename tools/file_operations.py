import glob
import xml.etree.cElementTree as ET


def list_files():
    files_source = './xl_source/*.xlsx'
    files_list = glob.glob(files_source)
    return files_list


def skip_start_rows(iter_rows, number_of_rows_to_skip_at_start):
    for _ in range(number_of_rows_to_skip_at_start):
        next(iter_rows)


def take_file_name_out_of_path(file_path):
    fixed_file_name = file_path[file_path.rfind('\\')+1:file_path.rfind('.xl')]
    return fixed_file_name


def write_tree_to_xml_file(file_path, main_test_suite, number_of_current_test_suite):
    tree = ET.ElementTree(main_test_suite)
    file_name = take_file_name_out_of_path(file_path)
    tree.write(f'xml_results/{file_name}_{number_of_current_test_suite}.xml', xml_declaration=True, encoding='utf-8')
    number_of_current_test_suite += 1
    return number_of_current_test_suite
