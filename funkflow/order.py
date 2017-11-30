#!/usr/bin/env python3

from enum import Enum
from collections import namedtuple

State = Enum('State', 'new partially_filled filled over_filled')
Event = Enum('Event', 'fill cancel')
Order = namedtuple('Order', 'quantity leaves_quantity state previous')

transitions = {
  State.new: {
    Event.fill: [
                 (lambda o: o.leaves_quantity == 0, State.filled),
                 (lambda o: o.leaves.quantity > 0, State.partially_filled),
                 (lambda o: o.leaves_quantity < 0, State.over_filled)]},
  State.partially_filled: {
    Event.fill: [
                 (lambda o: o.leaves_quantity == 0, State.filled),
                 (lambda o: o.leaves.quantity > 0, State.partially_filled),
                 (lambda o: o.leaves_quantity < 0, State.over_filled)]}}

def new(quantity):
  return Order(quantity, quantity, State.new, None)

def fill(order, quantity):
  new_order = order._replace(leaves_quantity=order.leaves_quantity-quantity)
  for guard,new_state in transitions[order.state][Event.fill]:
    if guard(new_order):
      return new_order._replace(state=new_state, previous=(order,Event.fill))
  return new_order
