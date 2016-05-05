# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class SubscriptionCancellationFailure(Exception):
    pass


class SubscriptionUpdateFailure(Exception):
    pass


class MultipleSubscriptionException(Exception):
    pass


class StripeObjectManipulationException(Exception):
    pass


class CustomerDoesNotExistLocallyException(Exception):
    pass
