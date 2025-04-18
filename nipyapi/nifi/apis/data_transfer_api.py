"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
import os
import re

from ..configuration import Configuration
from ..api_client import ApiClient


class DataTransferApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def commit_input_port_transaction(self, response_code, port_id, transaction_id, **kwargs):
        """
        Commit or cancel the specified transaction
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commit_input_port_transaction(response_code, port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int response_code: The response code. Available values are BAD_CHECKSUM(19), CONFIRM_TRANSACTION(12) or CANCEL_TRANSACTION(15). (required)
        :param str port_id: The input port id. (required)
        :param str transaction_id: The transaction id. (required)
        :return: TransactionResultEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.commit_input_port_transaction_with_http_info(response_code, port_id, transaction_id, **kwargs)
        else:
            (data) = self.commit_input_port_transaction_with_http_info(response_code, port_id, transaction_id, **kwargs)
            return data

    def commit_input_port_transaction_with_http_info(self, response_code, port_id, transaction_id, **kwargs):
        """
        Commit or cancel the specified transaction
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commit_input_port_transaction_with_http_info(response_code, port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int response_code: The response code. Available values are BAD_CHECKSUM(19), CONFIRM_TRANSACTION(12) or CANCEL_TRANSACTION(15). (required)
        :param str port_id: The input port id. (required)
        :param str transaction_id: The transaction id. (required)
        :return: TransactionResultEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['response_code', 'port_id', 'transaction_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commit_input_port_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'response_code' is set
        if ('response_code' not in params) or (params['response_code'] is None):
            raise ValueError("Missing the required parameter `response_code` when calling `commit_input_port_transaction`")
        # verify the required parameter 'port_id' is set
        if ('port_id' not in params) or (params['port_id'] is None):
            raise ValueError("Missing the required parameter `port_id` when calling `commit_input_port_transaction`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `commit_input_port_transaction`")


        collection_formats = {}

        path_params = {}
        if 'port_id' in params:
            path_params['portId'] = params['port_id']
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']

        query_params = []
        if 'response_code' in params:
            query_params.append(('responseCode', params['response_code']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/octet-stream'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/data-transfer/input-ports/{portId}/transactions/{transactionId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TransactionResultEntity',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def commit_output_port_transaction(self, response_code, checksum, port_id, transaction_id, **kwargs):
        """
        Commit or cancel the specified transaction
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commit_output_port_transaction(response_code, checksum, port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int response_code: The response code. Available values are CONFIRM_TRANSACTION(12) or CANCEL_TRANSACTION(15). (required)
        :param str checksum: A checksum calculated at client side using CRC32 to check flow file content integrity. It must match with the value calculated at server side. (required)
        :param str port_id: The output port id. (required)
        :param str transaction_id: The transaction id. (required)
        :return: TransactionResultEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.commit_output_port_transaction_with_http_info(response_code, checksum, port_id, transaction_id, **kwargs)
        else:
            (data) = self.commit_output_port_transaction_with_http_info(response_code, checksum, port_id, transaction_id, **kwargs)
            return data

    def commit_output_port_transaction_with_http_info(self, response_code, checksum, port_id, transaction_id, **kwargs):
        """
        Commit or cancel the specified transaction
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commit_output_port_transaction_with_http_info(response_code, checksum, port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int response_code: The response code. Available values are CONFIRM_TRANSACTION(12) or CANCEL_TRANSACTION(15). (required)
        :param str checksum: A checksum calculated at client side using CRC32 to check flow file content integrity. It must match with the value calculated at server side. (required)
        :param str port_id: The output port id. (required)
        :param str transaction_id: The transaction id. (required)
        :return: TransactionResultEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['response_code', 'checksum', 'port_id', 'transaction_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commit_output_port_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'response_code' is set
        if ('response_code' not in params) or (params['response_code'] is None):
            raise ValueError("Missing the required parameter `response_code` when calling `commit_output_port_transaction`")
        # verify the required parameter 'checksum' is set
        if ('checksum' not in params) or (params['checksum'] is None):
            raise ValueError("Missing the required parameter `checksum` when calling `commit_output_port_transaction`")
        # verify the required parameter 'port_id' is set
        if ('port_id' not in params) or (params['port_id'] is None):
            raise ValueError("Missing the required parameter `port_id` when calling `commit_output_port_transaction`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `commit_output_port_transaction`")


        collection_formats = {}

        path_params = {}
        if 'port_id' in params:
            path_params['portId'] = params['port_id']
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']

        query_params = []
        if 'response_code' in params:
            query_params.append(('responseCode', params['response_code']))
        if 'checksum' in params:
            query_params.append(('checksum', params['checksum']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/octet-stream'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/data-transfer/output-ports/{portId}/transactions/{transactionId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TransactionResultEntity',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_port_transaction(self, port_type, port_id, **kwargs):
        """
        Create a transaction to the specified output port or input port
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_port_transaction(port_type, port_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str port_type: The port type. (required)
        :param str port_id: (required)
        :return: TransactionResultEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_port_transaction_with_http_info(port_type, port_id, **kwargs)
        else:
            (data) = self.create_port_transaction_with_http_info(port_type, port_id, **kwargs)
            return data

    def create_port_transaction_with_http_info(self, port_type, port_id, **kwargs):
        """
        Create a transaction to the specified output port or input port
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_port_transaction_with_http_info(port_type, port_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str port_type: The port type. (required)
        :param str port_id: (required)
        :return: TransactionResultEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['port_type', 'port_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_port_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'port_type' is set
        if ('port_type' not in params) or (params['port_type'] is None):
            raise ValueError("Missing the required parameter `port_type` when calling `create_port_transaction`")
        # verify the required parameter 'port_id' is set
        if ('port_id' not in params) or (params['port_id'] is None):
            raise ValueError("Missing the required parameter `port_id` when calling `create_port_transaction`")


        collection_formats = {}

        path_params = {}
        if 'port_type' in params:
            path_params['portType'] = params['port_type']
        if 'port_id' in params:
            path_params['portId'] = params['port_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/data-transfer/{portType}/{portId}/transactions', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TransactionResultEntity',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def extend_input_port_transaction_ttl(self, port_id, transaction_id, **kwargs):
        """
        Extend transaction TTL
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.extend_input_port_transaction_ttl(port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str port_id: (required)
        :param str transaction_id: (required)
        :return: TransactionResultEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.extend_input_port_transaction_ttl_with_http_info(port_id, transaction_id, **kwargs)
        else:
            (data) = self.extend_input_port_transaction_ttl_with_http_info(port_id, transaction_id, **kwargs)
            return data

    def extend_input_port_transaction_ttl_with_http_info(self, port_id, transaction_id, **kwargs):
        """
        Extend transaction TTL
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.extend_input_port_transaction_ttl_with_http_info(port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str port_id: (required)
        :param str transaction_id: (required)
        :return: TransactionResultEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['port_id', 'transaction_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method extend_input_port_transaction_ttl" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'port_id' is set
        if ('port_id' not in params) or (params['port_id'] is None):
            raise ValueError("Missing the required parameter `port_id` when calling `extend_input_port_transaction_ttl`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `extend_input_port_transaction_ttl`")


        collection_formats = {}

        path_params = {}
        if 'port_id' in params:
            path_params['portId'] = params['port_id']
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/data-transfer/input-ports/{portId}/transactions/{transactionId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TransactionResultEntity',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def extend_output_port_transaction_ttl(self, port_id, transaction_id, **kwargs):
        """
        Extend transaction TTL
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.extend_output_port_transaction_ttl(port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str port_id: (required)
        :param str transaction_id: (required)
        :return: TransactionResultEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.extend_output_port_transaction_ttl_with_http_info(port_id, transaction_id, **kwargs)
        else:
            (data) = self.extend_output_port_transaction_ttl_with_http_info(port_id, transaction_id, **kwargs)
            return data

    def extend_output_port_transaction_ttl_with_http_info(self, port_id, transaction_id, **kwargs):
        """
        Extend transaction TTL
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.extend_output_port_transaction_ttl_with_http_info(port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str port_id: (required)
        :param str transaction_id: (required)
        :return: TransactionResultEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['port_id', 'transaction_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method extend_output_port_transaction_ttl" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'port_id' is set
        if ('port_id' not in params) or (params['port_id'] is None):
            raise ValueError("Missing the required parameter `port_id` when calling `extend_output_port_transaction_ttl`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `extend_output_port_transaction_ttl`")


        collection_formats = {}

        path_params = {}
        if 'port_id' in params:
            path_params['portId'] = params['port_id']
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/data-transfer/output-ports/{portId}/transactions/{transactionId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TransactionResultEntity',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def receive_flow_files(self, port_id, transaction_id, **kwargs):
        """
        Transfer flow files to the input port
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.receive_flow_files(port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str port_id: The input port id. (required)
        :param str transaction_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.receive_flow_files_with_http_info(port_id, transaction_id, **kwargs)
        else:
            (data) = self.receive_flow_files_with_http_info(port_id, transaction_id, **kwargs)
            return data

    def receive_flow_files_with_http_info(self, port_id, transaction_id, **kwargs):
        """
        Transfer flow files to the input port
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.receive_flow_files_with_http_info(port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str port_id: The input port id. (required)
        :param str transaction_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['port_id', 'transaction_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method receive_flow_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'port_id' is set
        if ('port_id' not in params) or (params['port_id'] is None):
            raise ValueError("Missing the required parameter `port_id` when calling `receive_flow_files`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `receive_flow_files`")


        collection_formats = {}

        path_params = {}
        if 'port_id' in params:
            path_params['portId'] = params['port_id']
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/octet-stream'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/data-transfer/input-ports/{portId}/transactions/{transactionId}/flow-files', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def transfer_flow_files(self, port_id, transaction_id, **kwargs):
        """
        Transfer flow files from the output port
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.transfer_flow_files(port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str port_id: The output port id. (required)
        :param str transaction_id: (required)
        :return: StreamingOutput
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.transfer_flow_files_with_http_info(port_id, transaction_id, **kwargs)
        else:
            (data) = self.transfer_flow_files_with_http_info(port_id, transaction_id, **kwargs)
            return data

    def transfer_flow_files_with_http_info(self, port_id, transaction_id, **kwargs):
        """
        Transfer flow files from the output port
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.transfer_flow_files_with_http_info(port_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str port_id: The output port id. (required)
        :param str transaction_id: (required)
        :return: StreamingOutput
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['port_id', 'transaction_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfer_flow_files" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'port_id' is set
        if ('port_id' not in params) or (params['port_id'] is None):
            raise ValueError("Missing the required parameter `port_id` when calling `transfer_flow_files`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `transfer_flow_files`")


        collection_formats = {}

        path_params = {}
        if 'port_id' in params:
            path_params['portId'] = params['port_id']
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/octet-stream'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/data-transfer/output-ports/{portId}/transactions/{transactionId}/flow-files', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StreamingOutput',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
