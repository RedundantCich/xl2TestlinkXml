import xml.etree.cElementTree as ET
from openpyxl import load_workbook
from tools import file_operations
from config import reader_config as cfg


def xl_to_xml_for_testlink(columns_in_use: dict, rows_to_skip: int, folder_xl_file_list: str) -> None:
    for file_name in folder_xl_file_list:
        workbook = load_workbook(file_name)
        iter_rows = workbook.active.iter_rows(min_row=1+rows_to_skip)

        main_test_suite = None
        number_of_current_test_suite = 1

        for row in iter_rows:
            for column in row:
                cell_value = column.value
                if cell_value is not None:
                    if column.column_letter in columns_in_use:
                        column_name = columns_in_use[column.column_letter]["column_name"]
                        xml_designation = columns_in_use[column.column_letter]["column_role"]
                    else:
                        continue

                    if xml_designation == 'main_test_suite':
                        if main_test_suite is not None:
                            file_operations.write_tree_to_xml_file(
                                file_name, main_test_suite, number_of_current_test_suite)
                            number_of_current_test_suite += 1
                        main_test_suite = ET.Element(column_name, name=cell_value)
                        parent_of_test_case = main_test_suite
                    elif xml_designation == 'sub_test_suite':
                        parent_of_test_case = ET.SubElement(main_test_suite, column_name, name=cell_value)
                    elif xml_designation == 'test_case':
                        test_case = ET.SubElement(parent_of_test_case, column_name, name=cell_value)
                    elif xml_designation == 'in_between':
                        ET.SubElement(test_case, column_name).text = str(cell_value)
                    elif xml_designation == 'preconditions':
                        ET.SubElement(test_case, column_name).text = str(cell_value)
                        steps = ET.SubElement(test_case, 'steps')
                        case_step = 1
                    elif xml_designation == 'actions':
                        step = ET.SubElement(steps, 'step')
                        ET.SubElement(step, 'step_number').text = str(case_step)
                        ET.SubElement(step, column_name).text = str(cell_value)
                    elif xml_designation == 'expected_results':
                        ET.SubElement(step, column_name).text = str(cell_value)
                        case_step += 1

        file_operations.write_tree_to_xml_file(
            file_name, main_test_suite, number_of_current_test_suite)
        number_of_current_test_suite += 1


if __name__ == "__main__":
    folder_xl_file_list = file_operations.list_files(cfg.file_format)
    xl_to_xml_for_testlink(
        cfg.columns_in_use, cfg.rows_to_skip, folder_xl_file_list)
