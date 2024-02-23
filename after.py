"""
Basic video exporting example
"""

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")


class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")


class CreateExporter(ABC):
    """Class to create exporters based on the desired quality."""

    @abstractmethod
    def create_video_exporter(self) -> VideoExporter:
        """Creates video exporter based on the desired quality."""
        pass

    @abstractmethod
    def create_audio_exporter(self) -> AudioExporter:
        """Creates audio exporter based on the desired quality."""
        pass


class CreateHighQualityExporter(CreateExporter):
    """Class to create exporters based for high quality output."""

    def create_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def create_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


class CreateLowQualityExporter(CreateExporter):
    """Class to create exporters based for low quality output."""

    def create_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def create_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class CreateMasterQualityExporter(CreateExporter):
    """Class to create exporters based for master quality output."""

    def create_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def create_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def get_exporter_from_output_quality() -> CreateExporter:
    """Get desired output quality from user and creates exporter based on the desired quality."""
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in {"low", "high", "master"}:
            break
        print(f"Unknown output quality option: {export_quality}.")

    if export_quality == "low":
        return CreateLowQualityExporter()
    if export_quality == "high":
        return CreateHighQualityExporter()
    if export_quality == "master":
        return CreateMasterQualityExporter()


def prepare_export(exporter: CreateExporter, video_data, audio_data) -> None:
    """Prepare the export based on the desired quality."""
    video_exporter = exporter.create_video_exporter()
    audio_exporter = exporter.create_audio_exporter()
    video_exporter.prepare_export(video_data)
    audio_exporter.prepare_export(audio_data)


def do_export(exporter: CreateExporter, folder: pathlib.Path) -> None:
    """Do the export based on the desired quality."""
    video_exporter = exporter.create_video_exporter()
    audio_exporter = exporter.create_audio_exporter()
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


def main() -> None:
    """Main function."""

    # create the exporter from the desired output quality
    exporter = get_exporter_from_output_quality()

    # prepare export
    prepare_export(exporter, "placeholder_for_video_data", "placeholder_for_audio_data")

    # do the export
    do_export(exporter, pathlib.Path("/usr/tmp/video"))


if __name__ == "__main__":
    main()
