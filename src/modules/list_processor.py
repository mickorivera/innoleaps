from typing import List


class ListProcessor:
    @staticmethod
    def flatten(input_list: List[List]) -> List:
        if type(input_list) != list:
            raise ValueError(
                f"Input is not an instance of a list: {input_list}"
            )

        output_list = []
        if len(input_list) == 0:
            return []

        if type(input_list[0]) != list:
            raise ValueError(
                f"An item is not an instance of a list: {input_list[0]}"
            )

        output_list.extend(input_list[0])
        output_list.extend(ListProcessor.flatten(input_list[1:]))
        return output_list
