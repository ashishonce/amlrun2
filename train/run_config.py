from azureml.core import ComputeTarget
from azureml.train.estimator import Estimator


def main(workspace):
    # Load compute target
    print("Loading compute target")
    compute_target = ComputeTarget(
        workspace=workspace,
        name="mycluster"
    )

    # Load script parameters
    print("Loading script parameters")
    script_params = {
        "--kernel": "linear",
        "--penalty": 1.0
    }

    # Create experiment config
    print("Creating experiment config")
    estimator = Estimator(
        source_directory="src/train",
        entry_script="train.py",
        script_params=script_params,
        compute_target=compute_target,
        conda_dependencies_file="environment.yml"
    )
    return estimator