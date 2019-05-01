import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-restaurantlist',
  templateUrl: './restaurantlist.component.html',
  styleUrls: ['./restaurantlist.component.css']
})
export class RestaurantlistComponent implements OnInit {

  restaurants = [1, 2, 3, 4, 5, 6]

  constructor() { }

  ngOnInit() {
  }

}
