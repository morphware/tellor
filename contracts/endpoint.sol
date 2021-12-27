// SPDX-License-Identifier: MIT
pragma solidity 0.8.3;

import "./ITellor.sol";
import "./SafeMath.sol";
import "./UsingTellor.sol";
import "./TellorPlayground.sol";

contract Endpoint is UsingTellor {
	using SafeMath for uint256;

	// endpoint
	bytes32 public _endpoint;
	uint256 public value;

    constructor(address payable _tellor) {
        tellor = ITellor(_tellor);
    }

    function getEndpoint(bytes32 _endpoint) returns (bytes32) {
        return _endpoint;
	
    }
    
    function getDataBefore(uint256 _requestId, uint256 _timestamp)
        public
        view
        returns (
            bool _ifRetrieve,
            uint256 _value,
            uint256 _timestampRetrieved
        )
    {
        (bool _found, uint256 _index) =
            getIndexForDataBefore(_requestId, _timestamp);
        if (!_found) return (false, 0, 0);
        uint256 _time =
            tellor.getTimestampbyRequestIDandIndex(_requestId, _index);
        _value = tellor.retrieveData(_requestId, _time);
        //If value is diputed it'll return zero
        if (_value > 0) return (true, _value, _time);
        return (false, 0, 0);
      }
    }
