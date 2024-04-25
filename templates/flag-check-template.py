data = {
  "title": "TEST TEMPLATE",
  "checks": [
    {
      "name": "TEST 1",
      "description": "test",
      "type": "adapter_check",
      "adapter_name": "eth0",
      "success_flag" : "FLAG TEST",
      "suggestions": ["test"]
    },
    {
      "name": "TEST 2",
      "description": "test",
      "type": "subnet_check",
      "subnet": "192.168.1.1",
      "adapter_name": "eth0",
      "success_flag" : "FLAGHERE",
      "suggestions": ["test"]
    }
  ]
}