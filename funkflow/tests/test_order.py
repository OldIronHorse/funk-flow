#!/usr/bin/env python3

from unittest import TestCase
from funkflow.order import Order, State, new, Event, fill


TestCase.maxDiff=None

class TestOrder(TestCase):
  maxDiff = None
  def test_new(self):
    self.assertEqual(Order(quantity=100, 
                           leaves_quantity=100, 
                           state=State.new, 
                           previous=None),
                     new(100))

  def test_single_fill(self):
    self.maxDiff = None
    self.assertEqual(Order(quantity=100, 
                           leaves_quantity=0, 
                           state=State.filled, 
                           previous=(Order(quantity=100, 
                                      leaves_quantity=100, 
                                      state=State.new, 
                                      previous=None), Event.fill)),
                     fill(new(100), 100))
