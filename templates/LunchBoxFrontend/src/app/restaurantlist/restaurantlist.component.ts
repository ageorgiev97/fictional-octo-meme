import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api-service/api.service';

@Component({
  selector: 'app-restaurantlist',
  templateUrl: './restaurantlist.component.html',
  styleUrls: ['./restaurantlist.component.css']
})
export class RestaurantlistComponent implements OnInit {

  restaurants

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.api.getAllRestaurants().subscribe(result => {
      this.restaurants = result;
    })
  }

}
