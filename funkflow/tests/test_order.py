#!/usr/bin/env python3

from unittest import TestCase
from funkflow.order import Order, State, new, Event, fill

class TestOrder(TestCase):
  def test_new(self):
    self.assertEqual(Order(quantity=100, 
                           leaves_quantity=100, 
                           state=State.new, 
                           previous=None),
                     new(100))

  def test_single_fill(self):
    self.assertEqual(Order(quantity=100, 
                           leaves_quantity=0, 
                           state=State.filled, 
                           previous=(Order(quantity=100, 
                                      leaves_quantity=100, 
                                      state=State.new, 
                                      previous=None), Event.fill)),
                     fill(new(100), 100))

  def test_single_partial_fill(self):
    self.assertEqual(Order(quantity=100, 
                           leaves_quantity=40, 
                           state=State.partially_filled, 
                           previous=(Order(quantity=100, 
                                      leaves_quantity=100, 
                                      state=State.new, 
                                      previous=None), Event.fill)),
                     fill(new(100), 60))

  def test_multiple_fills(self):
    o = new(100)
    o = fill(o, 40)
    o = fill(o, 60)
    self.assertEqual(Order(quantity=100,
                           leaves_quantity=0,
                           state=State.filled,
                           previous=(Order(quantity=100,
                                           leaves_quantity=60,
                                           state=State.partially_filled,
                                           previous=(Order(quantity=100,
                                                           leaves_quantity=100,
                                                           state=State.new,
                                                           previous=None),
                                                     Event.fill)),
                                     Event.fill)),
                     o)

  def test_over_fill(self):
    o = new(100)
    o = fill(o, 60)
    o = fill(o, 60)
    self.assertEqual(Order(quantity=100,
                           leaves_quantity=-20,
                           state=State.over_filled,
                           previous=(Order(quantity=100,
                                           leaves_quantity=40,
                                           state=State.partially_filled,
                                           previous=(Order(quantity=100,
                                                           leaves_quantity=100,
                                                           state=State.new,
                                                           previous=None),
                                                     Event.fill)),
                                     Event.fill)),
                     o)
