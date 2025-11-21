from typing import Dict, List

workflow_in = {
    "prepare_pin_data": [],  # 1
    "prepare_board_data": [],  # 2
    "compute_pin_metrics": ["prepare_pin_data"],  # 3
    "compute_pin_and_board_metrics": ["prepare_pin_data", "prepare_board_data"],  # 4
    "compute_board_metrics": ["prepare_board_data"],  # 5
    "publish_metrics": [
        "compute_pin_metrics",
        "compute_board_metrics",
        "compute_pin_and_board_metrics",
    ],  # 6
}

runtimes_in = {
    "prepare_pin_data": (5),
    "prepare_board_data": (10),
    "compute_pin_metrics": (400),
    "compute_pin_and_board_metrics": (900),
    "compute_board_metrics": (600),
    "publish_metrics": (70),
}


class CriticalPath(object):

    def __init__(self, workflow: Dict[str, List[str]], runtimes: Dict[str, int]):
        self.workflow = workflow
        self.runtimes = runtimes

    def find_critical_path(self, task_name) -> (int, List[str]):
        return self.find_critical_path_traverse([task_name], self.runtimes[task_name])

    def find_critical_path_traverse(self, critical_path, cost: int) -> (int, List[str]):
        if not self.workflow[critical_path[-1]]:
            return cost, critical_path
        max_cost = 0
        max_critical_path = []
        for task in self.workflow[critical_path[-1]]:
            new_critical_path = critical_path.copy()
            new_critical_path.append(task)
            path_cost, path = self.find_critical_path_traverse(
                new_critical_path, cost + self.runtimes[task] + 1
            )
            if path_cost > max_cost:
                max_cost = path_cost
                max_critical_path = path
        return max_cost, max_critical_path


print(CriticalPath(workflow_in, runtimes_in).find_critical_path("publish_metrics"))
