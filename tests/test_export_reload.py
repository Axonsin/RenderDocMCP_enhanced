"""New export modules must refresh after their shared exception dependencies."""
import ast
from pathlib import Path


def test_export_modules_participate_in_ordered_extension_reload():
    root=Path(__file__).resolve().parents[1]
    tree=ast.parse((root/'renderdoc_extension/__init__.py').read_text(encoding='utf-8'))
    modules=next(ast.literal_eval(node.value) for node in tree.body
                 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='_RELOAD_MODULES' for t in node.targets))
    for dependency,target in [('job_service','export_checkpoint'),('job_service','batch_export'),
                              ('constant_export','batch_export'),('investigation_service','batch_export'),
                              ('export_checkpoint','batch_export'),('batch_export','batch_service')]:
        assert modules.index('.services.'+dependency)<modules.index('.services.'+target)
