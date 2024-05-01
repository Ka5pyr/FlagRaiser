data = {
  "title": "TEST TEMPLATE",
  "checks": [
    {
      "name": "TEST 1",
      "description": "test",
      "type": "adapter_check",
      "adapter_name": "eth4",
      "success_flag": "FLAG TEST",
      "print_success": True,
      "suggestions": ["test"]
    },
    {
      "name": "TEST 2",
      "description": "test",
      "type": "subnet_check",
      "subnet": "192.168.1.1",
      "adapter_name": "eth0",
      "success_flag" : "FLAGHERE",
      "print_success": False,
      "suggestions": ["test"]
    }
  ]
}