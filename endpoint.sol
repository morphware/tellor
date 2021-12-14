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


	event TipAdded(
        address indexed _sender,
        uint256 indexed _requestId,
        uint256 _tip,
        uint256 _totalTips
    );

    constructor(address payable _tellor) {
        tellor = ITellor(_tellor);
    }

    function submitValue(uint256 _requestId, bytes memory _value) external {
    	_requestId = requestId;
    	// WOuld Enpoint go here?
    }

    getCurrentValue()

	/**
     * @dev Add tip to a request ID
     * @param _requestId being requested to be mined
     * @param _tip amount the requester is willing to pay to be get on queue. Miners
     * mine the ID with the highest tip
    */
    function addTip(uint256 _requestId, uint256 _tip) external {
        require(_requestId != 0, "RequestId is 0");
        require(_tip != 0, "Tip should be greater than 0");
        uint256 _count = uints[_REQUEST_COUNT] + 1;
        if (_requestId == _count) {
            uints[_REQUEST_COUNT] = _count;
        } else {
            require(_requestId < _count, "RequestId is not less than count");
        }
        _doBurn(msg.sender, _tip);
        //Update the information for the request that should be mined next based on the tip submitted
        _updateOnDeck(_requestId, _tip);
        emit TipAdded(
            msg.sender,
            _requestId,
            _tip,
            requestDetails[_requestId].apiUintVars[_TOTAL_TIP]
        );
    }

}