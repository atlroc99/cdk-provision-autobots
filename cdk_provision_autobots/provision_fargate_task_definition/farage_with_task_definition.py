from aws_cdk import (core,
                     aws_iam as _iam,
                     aws_ec2 as _ec2,
                     aws_ecs as _ecs,
                     aws_ecs_patterns as _ecs_patterns,
                     aws_elasticloadbalancingv2 as elb,
                     aws_logs as _logs)


class FargateWithTaskDefinition(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        _myVpc = _ec2.Vpc(self, "myVpcID", max_azs=2, nat_gateways=1)
        _ecs_cluster_2 = _ecs.Cluster(self, 'cdkFargateCluster', vpc=_myVpc, cluster_name="CdkFargate_Cluser_2")
        _UI_SERVICE = 'thiethaa/alc-autobots-ui'
        # _CHECKLIST_SERVICE = ''

        # ecr.amazonaws.com
        # ecs-tasks.amazonaws.com
        # ecs.amazonaws.com

        _ecs_patterns.ApplicationLoadBalancedFargateService(self, "fargateServiceSecondtry",
                                                            cluster=_ecs_cluster_2,
                                                            cpu=512,
                                                            desired_count=2,
                                                            memory_limit_mib=1024,
                                                            public_load_balancer=True,
                                                            task_image_options=_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                                image=_ecs.ContainerImage.from_registry(_UI_SERVICE)))

    """   
    _container_image = _ecs.ContainerImage.from_registry(_UI_SERVICE)
       _task_role = _iam.Role(self,
                              "taskExeRoleID",
                              # role_name="ecsTaskExecutionRole",
                              assumed_by=_iam.ServicePrincipal(service='ecs-tasks.amazonaws.com'))



       alb_task_image_options = _ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
           # "taskImageOptions",
           image=_container_image,
           container_port=4040,
           container_name="autobots-UI-container",
           task_role=_task_role,
           enable_logging=True)

       # A Fargate service running on an ECS cluster fronted by an application load balancer
       app_load_balanced_fargate_service = _ecs_patterns.ApplicationLoadBalancedFargateService(self,
                                                                                               'FargateServiceALB',
                                                                                               cpu=256,
                                                                                               memory_limit_mib=512,
                                                                                               cluster=_ecs_cluster_2,
                                                                                               desired_count=1,
                                                                                               # listener_port=4040,
                                                                                               open_listener=True,
                                                                                               min_healthy_percent=0,
                                                                                               protocol=elb.ApplicationProtocol.HTTP,
                                                                                               service_name='autobots_ui',

                                                                                               task_image_options=alb_task_image_options)
       
       
       

       # app_load_balanced_fargate_service.task_definition.execution_role.role_name("ecsTaskExecutionRole")

       app_load_balancer_dns_name = app_load_balanced_fargate_service.load_balancer.load_balancer_dns_name

       alb_cfn_output = core.CfnOutput(self, "albDNSName", value=F"{app_load_balancer_dns_name}",
                                       description="Application load balancer DNS Name for autobots UI")
       listener_output = core.CfnOutput(self, "albListener", value=F"{app_load_balanced_fargate_service.listener}",
                                        description="app_load_balanced_fargate_service.listener")

       # _logs.LogGroup(self, "albFaragetTaskDefLogGroup", log_group_name=f"{}",
       #                removal_policy=core.RemovalPolicy.DESTROY)
"""
