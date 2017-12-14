$cred = New-Object System.Management.Automation.PSCredential("hzit@hzbj.partner.onmschina.cn",(ConvertTo-SecureString "57192622@hmkdl9" -AsPlainText -Force))
Add-AzureRmAccount -Environment AzureChinaCloud -Credential $cred
#Login-AzureRmAccount -Environment AzureChinaCloud
#Get-AzureRmResourceGroup
#Save-AzureProfile -Path "C:\Users\Administrator\Desktop\azure迁移\login.json"
#Select-AzureProfile
Select-AzureSubscription -SubscriptionName 标准预付费服务
#1.检索Azure中的负载均衡器
$lb= get-azurermloadbalancer -name $args[0] -resourcegroupname cloud-p2p
 
#2.将后端地址池添加到变量
$backend=Get-AzureRmLoadBalancerBackendAddressPoolConfig -name $args[1]  -LoadBalancer $lb
 
#3.将要移除的网络接口加载后变量中名称为$nic1
$nic1 = get-azurermnetworkinterface -name $args[2] -resourcegroupname cloud-p2p
 
#4.更改网络接口上的后端配置
$nic1.IpConfigurations[0].LoadBalancerBackendAddressPools=$null
 
#5.更新网络接口使配置生效
Set-AzureRmNetworkInterface -NetworkInterface $nic1


