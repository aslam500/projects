#bard failed
from vmaf import VmafModel

model_path = 'path_to_vmaf_v0.6.1.pkl'

vmaf_model = VmafModel(model_path=model_path)

ref_video_path = 'path_to_reference_video.mp4'
distorted_video_path = 'path_to_distorted_video.mp4'

vmaf_score = vmaf_model.compute_vmaf(ref_path=ref_video_path, dis_path=distorted_video_path)

print(f"VMAF Score: {vmaf_score}")
