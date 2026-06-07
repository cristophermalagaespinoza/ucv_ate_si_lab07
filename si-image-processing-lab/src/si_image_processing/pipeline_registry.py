from kedro.pipeline import Pipeline

from si_image_processing.pipelines.image_processing.pipeline import (
    create_pipeline as create_image_processing_pipeline,
)


def register_pipelines() -> dict[str, Pipeline]:
    image_processing_pipeline = create_image_processing_pipeline()

    return {
        "image_processing": image_processing_pipeline,
        "__default__": image_processing_pipeline,
    }