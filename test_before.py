# Black box test for code in main() in before.py

import before
import unittest
from unittest.mock import patch, Mock, call
from io import StringIO


# Test logic for main() in before.py
# Call main() in before.py, input dummy data (low, high, master) and check if the respective audio and video exporters are created and the expected prepare_export() and do_export() methods are called for each exporter


class TestMain(unittest.TestCase):

    maxDiff = None

    @patch("builtins.input", side_effect=["low"])
    def test_main(self, mock_input):
        with patch("before.AACAudioExporter.prepare_export") as mock_prepare_export:
            with patch(
                "before.H264BPVideoExporter.prepare_export"
            ) as mock_prepare_export_video:
                with patch("before.AACAudioExporter.do_export") as mock_do_export:
                    with patch(
                        "before.H264BPVideoExporter.do_export"
                    ) as mock_do_export_video:
                        before.main()
                        mock_prepare_export.assert_called_once()
                        mock_prepare_export_video.assert_called_once()
                        mock_do_export.assert_called_once()
                        mock_do_export_video.assert_called_once()

    @patch("builtins.input", side_effect=["high"])
    def test_main(self, mock_input):
        with patch("before.AACAudioExporter.prepare_export") as mock_prepare_export:
            with patch(
                "before.H264Hi422PVideoExporter.prepare_export"
            ) as mock_prepare_export_video:
                with patch("before.AACAudioExporter.do_export") as mock_do_export:
                    with patch(
                        "before.H264Hi422PVideoExporter.do_export"
                    ) as mock_do_export_video:
                        before.main()
                        mock_prepare_export.assert_called_once()
                        mock_prepare_export_video.assert_called_once()
                        mock_do_export.assert_called_once()
                        mock_do_export_video.assert_called_once()

    @patch("builtins.input", side_effect=["master"])
    def test_main(self, mock_input):
        with patch("before.WAVAudioExporter.prepare_export") as mock_prepare_export:
            with patch(
                "before.LosslessVideoExporter.prepare_export"
            ) as mock_prepare_export_video:
                with patch("before.WAVAudioExporter.do_export") as mock_do_export:
                    with patch(
                        "before.LosslessVideoExporter.do_export"
                    ) as mock_do_export_video:
                        before.main()
                        mock_prepare_export.assert_called_once()
                        mock_prepare_export_video.assert_called_once()
                        mock_do_export.assert_called_once()
                        mock_do_export_video.assert_called_once()

    # When the user enters an unknown option for export quality (random), the program should print "Unknown output quality option: random." and display the prompt again
    @patch(
        "builtins.input",
        side_effect=["random_string", "another_invalid", "still_invalid", "low"],
    )
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_with_invalid_input(self, mock_stdout, mock_input):
        # Call the main function
        before.main()
        # Check if the expected messages are printed to stdout. use format specifiers to replace the placeholders with the actual values
        expected_output = (
            "Unknown output quality option: random_string.\n"
            "Unknown output quality option: another_invalid.\n"
            "Unknown output quality option: still_invalid.\n"
            "Preparing video data for H.264 (Baseline) export.\n"
            "Preparing audio data for AAC export.\n"
            "Exporting video data in H.264 (Baseline) format to /usr/tmp/video.\n"
            "Exporting audio data in AAC format to /usr/tmp/video.\n"
        )
        actual_output = mock_stdout.getvalue()
        self.assertEqual(
            actual_output, expected_output, f"Actual output:\n{actual_output}"
        )


if __name__ == "__main__":
    unittest.main()
