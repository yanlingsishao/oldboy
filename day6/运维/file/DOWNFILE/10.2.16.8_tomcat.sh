#!/bin/bash
#auto install jdk+tomcat
#by wangqy 2016-08
T_FILES_DIR=apache-tomcat-8.0.11
T_FILES=apache-tomcat-8.0.11.tar.gz
T_URL=/home/hzjkit/
T_PREFIX=/usr/local/
J_FILES=jdk-7u67-linux-x64.rpm
PASSWD="v6Qn=!|9t9#rqxu/~d7l"
echo $PASSWD |sudo -S cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
echo $PASSWD |sudo -S rpm -ivh $T_URL$J_FILES
echo -e "\033[36mjava install sucessful\033[0m"
echo $PASSWD |sudo -S tar -zxvf $T_FILES -C $T_PREFIX
echo -e "\033[36m-------tomcat install sucessfully------\033[0m"
echo "huazhen@123"|sudo -S chmod 777 /etc/profile
echo "huazhen@123"|sudo -S sed -i 'N;78a\export JAVA_HOME=/usr/java/jdk1.7.0_67\nexport PATH=$PATH:$JAVA_HOME/bin\nexport CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib\nexport TOMCAT_HOME=/usr/local/apache-tomcat-8.0.11\nexport CATALINA_HOME=/usr/local/apache-tomcat-8.0.11' /etc/profile
source /etc/profile
echo $PASSWD |sudo -S chmod 644 /etc/profile
echo $PASSWD |sudo -S sed -i 'N;98a\JAVA_OPTS="-Xms512m -Xmx1024m -Xss1024K -server -Duser.timezone=GMT+08 -XX:PermSize=128m -XX:MaxPermSize=256m"' $T_PREFIX$T_FILES_DIR/bin/catalina.sh
echo "配置环境成功"

