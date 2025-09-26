from __future__ import annotations
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__

@_Jac.make_node(on_entry=[], on_exit=[])
@__jac_dataclass__(eq=False)
class Greeter:

    def lovejac(self) -> None:
        return 'With Jac, Python becomes even more awesome!'
_Jac.connect(left=_jac_here_(), right=Greeter, edge_spec=_Jac.build_edge(is_undirected=False, conn_type=None, conn_assign=None))
std.out(_jac_here_.lovejac())