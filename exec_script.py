import xml.etree.cElementTree as ET
from openpyxl import load_workbook
from tools import file_operations
from config import reader_config as cfg


def xl_to_xml_for_testlink(columns_in_use: dict, rows_to_skip: int, folder_xl_file_list: str) -> None:
    for file_name in folder_xl_file_list:
        workbook = load_workbook(file_name)
        iter_rows = workbook.active.iter_rows()
        file_operations.skip_start_rows(iter_rows, rows_to_skip)

        main_test_suite = None
        number_of_current_test_suite = 1

        for row in iter_rows:
            for column in row:
                cell_value = column.value
                if cell_value is not None:
                    if column.column_letter in columns_in_use:
                        column_name, xml_designation, additional_action = columns_in_use[
                            column.column_letter]
                    else:
                        continue

                    if xml_designation == 'main_parent':
                        if main_test_suite is not None:
                            number_of_current_test_suite = \
                                file_operations.write_tree_to_xml_file(
                                    file_name, main_test_suite, number_of_current_test_suite)
                        main_test_suite = ET.Element(
                            column_name, name=cell_value)
                        continue
                    elif xml_designation == 'sub_parent' and additional_action == 'optional_test_suite_present':
                        sub_test_suite = ET.SubElement(
                            main_test_suite, column_name, name=cell_value)
                        parent_of_test_case = sub_test_suite
                        continue
                    elif xml_designation == 'sub_parent' and additional_action == 'no_additional_actions':
                        if sub_test_suite is None:
                            parent_of_test_case = main_test_suite
                        test_case = ET.SubElement(
                            parent_of_test_case, column_name, name=cell_value)
                        continue
                    elif xml_designation == 'text_child':
                        ET.SubElement(test_case, column_name).text = str(
                            cell_value)

                    if additional_action == 'start_steps':
                        steps = ET.SubElement(test_case, 'steps')
                        case_step = 1
                    elif additional_action == 'start_single_step':
                        step = ET.SubElement(steps, 'step')
                        ET.SubElement(step, 'step_number').text = str(case_step)
                        ET.SubElement(step, column_name).text = str(cell_value)
                    elif additional_action == 'end_single_step':
                        ET.SubElement(step, column_name).text = str(cell_value)
                        case_step += 1

        number_of_current_test_suite = \
            file_operations.write_tree_to_xml_file(
                file_name, main_test_suite, number_of_current_test_suite)


if __name__ == "__main__":
    folder_xl_file_list = file_operations.list_files(cfg.file_format)
    xl_to_xml_for_testlink(
        cfg.columns_in_use, cfg.rows_to_skip, folder_xl_file_list)
