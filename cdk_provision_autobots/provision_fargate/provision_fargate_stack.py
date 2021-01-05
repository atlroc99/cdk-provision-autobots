from aws_cdk import (
    core,
    aws_ec2 as _ec2,
    aws_ecs as _ecs,
    aws_ecs_patterns as _ecs_patterns
)


class ProvisionFargateWithECSServiceStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create vpc where the Fargate and microservices will be deployed
        _my_vpc = _ec2.Vpc(self, "myVPCforContaines", max_azs=2, nat_gateways=1)

        # create the ecs cluster
        _ecs_cluster_with_fargate = _ecs.Cluster(self,
                                                 "myECSClusterForFargate",
                                                 cluster_name="cdk_autobots_cluster_fargate",
                                                 vpc=_my_vpc
                                                 )
        _ACCOUNT_ID = core.Aws.ACCOUNT_ID
        _REGION = core.Aws.REGION
        _DKR_ECR = 'dkr.ecr'
        _AMZ_AWS_DOT_COM = 'amazonaws.com'

        # 429506819373.dkr.ecr.us-east-1.amazonaws.com/alc-autobots-migration:checklist-service
        _CHECKLIST_SERVICE = 'alc-autobots-migration:checklist-service'

        # 429506819373.dkr.ecr.us-east-1.amazonaws.com/alc-autobots-migration:questionnaire-service
        _QUESTIONNAIRE_SERVICE = 'alc-autobots-migration:checklist-service'

        _UI_SERVICE = 'atlroc99/red-theme-ui:latest'

        """
        checklist_service_fargate = _ecs_patterns.ApplicationLoadBalancedFargateService(self,
                                                                                        "checklistService",
                                                                                        cluster=_ecs_cluster_with_fargate,
                                                                                        cpu=256,
                                                                                        memory_limit_mib=512,
                                                                                        desired_count=2,
                                                                                        public_load_balancer=True,
                                                                                        task_image_options=_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                                                            image=_ecs.ContainerImage.from_registry(
                                                                                                f"{_ACCOUNT_ID}.{_DKR_ECR}.{_REGION}.{_AMZ_AWS_DOT_COM}/{_CHECKLIST_SERVICE}")))

        # f"{account_no}.dkr.ecr.{us - east - 1}.amazonaws.com/alc-autobots-migration:checklist-service")))
        questionnarie_service_fargate = _ecs_patterns.ApplicationLoadBalancedFargateService(self,
                                                                                            "questionnaireService",
                                                                                            cluster=_ecs_cluster_with_fargate,
                                                                                            cpu=256,
                                                                                            memory_limit_mib=512,
                                                                                            desired_count=2,
                                                                                            public_load_balancer=True,
                                                                                            task_image_options=_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                                                                image=_ecs.ContainerImage.from_registry(
                                                                                                    f"{_ACCOUNT_ID}.{_DKR_ECR}.{_REGION}.{_AMZ_AWS_DOT_COM}/{_QUESTIONNAIRE_SERVICE}")))
        """
        # 429506819373.dkr.ecr.us-east-1.amazonaws.com/alc-autobots-migration:checklist-service

        migration_ui_service = _ecs_patterns.ApplicationLoadBalancedFargateService(self,
                                                                                   "migrationUI",
                                                                                   cluster=_ecs_cluster_with_fargate,
                                                                                   cpu=256,
                                                                                   memory_limit_mib=512,
                                                                                   desired_count=2,
                                                                                   public_load_balancer=True,
                                                                                   listener_port=4040,
                                                                                   task_image_options=_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                                                       image=_ecs.ContainerImage.from_registry(
                                                                                           f"{_UI_SERVICE}")))

        _ecs.PortMapping(container_port=4040, host_port=3000)


        # create serverless_web_service.target_group.configure_health_check(path="/")
        #
        #         fargate_out = core.CfnOutput(self,
        #                                      "fargateALBOutput",
        #                                      description="url for fargate cluster",
        #                                      value=f"{serverless_web_service.load_balancer.load_balancer_dns_name}")

        ui_output = core.CfnOutput(self, "uiOutputLink", description="link for ui", value=f"{migration_ui_service.load_balancer.load_balancer_dns_name}")