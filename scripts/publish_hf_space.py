from __future__ import annotations

import argparse
from pathlib import Path

from huggingface_hub import HfApi


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Upload Gradio Space files (app.py, requirements, README) to Hugging Face — không gồm dataset-upload."
    )
    parser.add_argument(
        "--space-repo",
        required=True,
        help="Space repo id, ví dụ YOUR_USERNAME/coupa-docs-semantic-search",
    )
    parser.add_argument(
        "--space-dir",
        default=str(Path(__file__).resolve().parents[1] / "output" / "hf-space-template"),
        help="Thư mục chứa app.py, requirements.txt, README.md (mặc định: output/hf-space-template)",
    )
    parser.add_argument("--private", action="store_true", help="Tạo Space private (nếu chưa tồn tại)")
    parser.add_argument(
        "--commit-message",
        default="Update Space app",
        help="Git commit message trên Hub",
    )
    args = parser.parse_args()

    space_dir = Path(args.space_dir).resolve()
    for name in ("app.py", "requirements.txt", "README.md"):
        if not (space_dir / name).exists():
            raise FileNotFoundError(f"Missing file: {space_dir / name}")

    api = HfApi()
    api.create_repo(
        repo_id=args.space_repo,
        repo_type="space",
        space_sdk="gradio",
        private=args.private,
        exist_ok=True,
    )
    api.upload_folder(
        repo_id=args.space_repo,
        repo_type="space",
        folder_path=str(space_dir),
        ignore_patterns=["dataset-upload/**", ".git/**"],
        commit_message=args.commit_message,
    )
    # ASCII-only: Windows cp1252 consoles break on Vietnamese.
    print(f"Uploaded Space: https://huggingface.co/spaces/{args.space_repo}")
    print("Optional: Space -> Settings -> Repository secrets -> add HF_TOKEN for Inference API (summarize/translate).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
