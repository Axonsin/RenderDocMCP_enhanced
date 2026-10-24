"""Explicit one-time download of torchvision's official AlexNet weights.
Evaluation itself never downloads. Cache remains inside this benchmark folder.
"""
import os,pathlib,re,hashlib,json
ROOT=pathlib.Path(__file__).resolve().parent
os.environ['TORCH_HOME']=str(ROOT/'cache/torch')
import torch,torchvision,lpips
from torchvision.models import AlexNet_Weights
url=AlexNet_Weights.IMAGENET1K_V1.url
target=pathlib.Path(torch.hub.get_dir())/'checkpoints'/url.rsplit('/',1)[1]
target.parent.mkdir(parents=True,exist_ok=True)
prefix=re.search(r'-([0-9a-f]+)\.',target.name).group(1)
if not target.exists():torch.hub.download_url_to_file(url,str(target),hash_prefix=prefix,progress=False)
digest=hashlib.sha256(target.read_bytes()).hexdigest()
if not digest.startswith(prefix):raise RuntimeError('AlexNet published checksum mismatch')
calibration=pathlib.Path(lpips.__file__).parent/'weights/v0.1/alex.pth'
record={'url':url,'backbone_sha256':digest,'calibration_sha256':hashlib.sha256(calibration.read_bytes()).hexdigest(),'torch':torch.__version__,'torchvision':torchvision.__version__,'cache':str(target)}
(ROOT/'metric-environment.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record,indent=2))
