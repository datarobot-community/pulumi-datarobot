# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

import os
import pathlib
import tempfile
import zipfile
from datetime import datetime

from datarobotx.idp.datasets import get_or_create_dataset_from_file


def upload_vector_database(
    token: str,
    endpoint: str,
    use_case_id: str,
    file_path: bytes | pathlib.Path,
    name: str,
) -> str:
    if isinstance(file_path, bytes):
        with tempfile.TemporaryDirectory() as tmpdir:
            # zip the files in the folder given by raw_files to a temporary zip file
            zip_file_path = pathlib.Path(tmpdir) / "vector_database.zip"
            # write the contents of the file_path to the zip file
            with open(zip_file_path, "wb") as f:
                f.write(file_path)

            vector_database_id = get_or_create_dataset_from_file(
                token=token,
                endpoint=endpoint,
                use_cases=use_case_id,
                file_path=str(zip_file_path),
                name=name,
            )
        return vector_database_id
    else:
        with tempfile.TemporaryDirectory() as tmpdir:
            # zip the files in the folder given by raw_files to a temporary zip file
            zip_file_path = pathlib.Path(tmpdir) / "vector_database.zip"
            date_time = datetime(2020, 1, 1, 12, 0)  # Creating a datetime object
            with zipfile.ZipFile(zip_file_path, "w") as zipf:
                # Walk through the directory
                for folderName, _, filenames in os.walk(str(file_path)):
                    for filename in filenames:
                        # Full path of the current file
                        filePath = os.path.join(folderName, filename)
                        # Archive name (relative path within the zip file)
                        arcname = os.path.relpath(filePath, start=str(file_path))

                        # ZipInfo object to handle metadata (like the timestamp)
                        zip_info = zipfile.ZipInfo(arcname)
                        zip_info.date_time = date_time.timetuple()[:6]
                        zip_info.compress_type = zipfile.ZIP_DEFLATED

                        # Read file contents and add them to the zip file with the fixed timestamp
                        with open(filePath, "rb") as f:
                            file_data = f.read()
                        zipf.writestr(zip_info, file_data)
            vector_database_id = get_or_create_dataset_from_file(
                token=token,
                endpoint=endpoint,
                use_cases=use_case_id,
                file_path=str(zip_file_path),
                name=name,
            )
        return vector_database_id
