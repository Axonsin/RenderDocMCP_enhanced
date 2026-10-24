"""Create an unfilled submission template. No fake telemetry, scores or artifacts."""
import argparse,datetime,json,pathlib,sys
from benchmark import TASKS
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--task',choices=TASKS,required=True);p.add_argument('--run-id',required=True);p.add_argument('--out',type=pathlib.Path,required=True);a=p.parse_args()
    if a.out.exists():raise SystemExit('Output already exists; choose a new run directory')
    case=json.loads((pathlib.Path(__file__).resolve().parents[1]/'dataset/case.json').read_text(encoding='utf-8'))
    a.out.mkdir(parents=True)
    run={'schema_version':1,'run_id':a.run_id,'task':a.task,'role':'candidate','outcome':'incomplete','experiment_id':case['case_id'],'condition_id':'REPLACE_WITH_MCP_MODEL_TOOL_CONDITION','protocol_id':case.get('protocol_id','rdoc-ss-frame2925-v2'),'repetition':1,'session_id':None,'capture_sha256':case['sha256'],
      'model':{'name':'REPLACE_WITH_ACTUAL_MODEL','version':None,'reasoning_effort':None},'mcp':{'version':None,'commit':None,'client':None,'tools_manifest':None},
      'started_at':None,'prompt_file':None,'replay_environment':{'device':None,'initial_condition':None,'cold_start':None},'artifacts':{},'log':None,
      'telemetry':{'wall_time_s':None,'input_tokens':None,'output_tokens':None,'tool_calls':None,'cost_usd':None},'phase_times_s':{'capture_load_transfer':None,'tool_execution':None,'remote_replay':None,'local_generation':None}}
    (a.out/'run.json').write_text(json.dumps(run,ensure_ascii=False,indent=2),encoding='utf-8')
    (a.out/'README.md').write_text('# 未运行提交模板\n\n这是待填写清单，不是实际结果。实际开始时记录started_at、session_id、模型、MCP、提示词与工具集合；每项时间缺失保持null。完成后声明真实产物相对路径与outcome。不要把裁判参考产物复制成候选结果。失败/中断也保留记录。\n',encoding='utf-8')
    print(a.out)
if __name__=='__main__':main()
