# Copyright 2016-2021, Pulumi Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from os import path
import unittest
from ..util import LanghostTest


class RemoteComponentDependenciesTest(LanghostTest):
    def test_remote_component_dependencies(self):
        self.run_test(
            program=path.join(self.base_path(), "remote_component_dependencies"),
            expected_resource_count=3,
        )

    def register_resource(
        self,
        _ctx,
        _dry_run,
        ty,
        name,
        _resource,
        _dependencies,
        _parent,
        _custom,
        protect,
        _provider,
        _property_deps,
        _delete_before_replace,
        _ignore_changes,
        _version,
        _import,
        _replace_on_changes,
        _providers,
        source_position,
    ):
        if name == "resA":
            self.assertEqual(len(_dependencies), 0, "resA dependencies")
        elif name == "resB":
            self.assertEqual(len(_dependencies), 1, "resB dependencies")
        elif name == "resC":
            self.assertEqual(len(_dependencies), 1, "resC dependencies")
            self.assertEqual(_parent, "resA", "resC parent")
        else:
            assert False

        return {
            "urn": name,
            "id": name,
            "object": {
                "outprop": "qux",
            },
        }
