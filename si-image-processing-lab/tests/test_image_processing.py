from pathlib import Path

from PIL import Image

from si_image_processing.pipelines.image_processing.nodes import process_image


def test_process_image(tmp_path):
    input_path = tmp_path / "marte.jpg"
    output_path = tmp_path / "test_output.jpg"

    Image.new("RGB", (100, 100), color="black").save(input_path)

    result = process_image(str(input_path), str(output_path))

    assert result == str(output_path)
    assert Path(result).exists()
