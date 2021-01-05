#!/usr/bin/env python3

from aws_cdk import core

from cdk_provision_autobots.cdk_provision_autobots_stack import CdkProvisionAutobotsStack

from cdk_provision_autobots.provision_fargate.provision_fargate_stack import ProvisionFargateWithECSServiceStack
from cdk_provision_autobots.provision_fargate_task_definition.farage_with_task_definition import FargateWithTaskDefinition

app = core.App()
# ProvisionFargateWithECSServiceStack(app, "cdk-provision-fargate")
# CdkProvisionAutobotsStack(app, "cdk-provision-autobots")
FargateWithTaskDefinition(app, 'fargate-task-definition')

app.synth()
