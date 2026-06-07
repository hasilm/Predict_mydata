from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path=str(Folder_name)+"/deployment",
    repo_id=str(HF_username)+"/"+str(App_name), # enter the Hugging Face username here
    repo_type="space",
    path_in_repo=""                          # optional: subfolder path inside the repo
)
