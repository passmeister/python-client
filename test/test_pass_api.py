# coding: utf-8

"""
    Demo Client for Passmeister Apple Wallet and Google Wallet API

    [www.passmeister.com](https://www.passmeister.com).  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.pass_api import PassApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPassApi(unittest.TestCase):
    """PassApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.pass_api.PassApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_or_update_pass(self):
        """Test case for create_or_update_pass

        This method creates or (if the pass id already exists) updates a pass, so you don't have to track ids and creation status of your passes.  # noqa: E501
        """
        pass

    def test_delete_pass(self):
        """Test case for delete_pass

        Delete pass by pass id.  # noqa: E501
        """
        pass

    def test_get_pass(self):
        """Test case for get_pass

        Get pass information by pass id.  # noqa: E501
        """
        pass

    def test_pass_list(self):
        """Test case for pass_list

        Retrieve the list of active pass ids for a given pass type.  # noqa: E501
        """
        pass

    def test_pass_sync(self):
        """Test case for pass_sync

        Send updates to all active passes for a given pass type.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()