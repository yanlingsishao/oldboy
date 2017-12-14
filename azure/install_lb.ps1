$cred = New-Object System.Management.Automation.PSCredential("hzit@hzbj.partner.onmschina.cn",(ConvertTo-SecureString "57192622@hmkdl9" -AsPlainText -Force))
Add-AzureRmAccount -Environment AzureChinaCloud -Credential $cred
Select-AzureSubscription -SubscriptionName 标准预付费服务
$lb= get-azurermloadbalancer -name $args[0] -resourcegroupname cloud-p2p
$backend=Get-AzureRmLoadBalancerBackendAddressPoolConfig -name $args[1]  -LoadBalancer $lb
$nic1 = get-azurermnetworkinterface -name $args[2] -resourcegroupname cloud-p2p
#升级完网站之后可参考如下添加网络接口到后端地址池
#向负载均衡器添加网络接口
#1.指定网卡上的后端配置
$nic1.IpConfigurations[0].LoadBalancerBackendAddressPools=$backend
 
#2.更新网络接口使配置生效
Set-AzureRmNetworkInterface -NetworkInterface $nic1

