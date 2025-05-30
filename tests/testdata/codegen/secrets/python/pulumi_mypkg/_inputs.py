# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = [
    'ConfigArgs',
    'ConfigArgsDict',
]

MYPY = False

if not MYPY:
    class ConfigArgsDict(TypedDict):
        foo: NotRequired[pulumi.Input[builtins.str]]
elif False:
    ConfigArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ConfigArgs:
    def __init__(__self__, *,
                 foo: Optional[pulumi.Input[builtins.str]] = None):
        if foo is not None:
            pulumi.set(__self__, "foo", foo)

    @property
    @pulumi.getter
    def foo(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "foo")

    @foo.setter
    def foo(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "foo", value)


