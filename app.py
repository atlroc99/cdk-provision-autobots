#!/usr/bin/env python3

from aws_cdk import core

from cdk_provision_autobots.cdk_provision_autobots_stack import CdkProvisionAutobotsStack


app = core.App()
CdkProvisionAutobotsStack(app, "cdk-provision-autobots")

app.synth()
