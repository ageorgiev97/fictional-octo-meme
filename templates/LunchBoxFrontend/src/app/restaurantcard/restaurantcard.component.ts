import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core';

@Component({
  selector: 'app-restaurantcard',
  templateUrl: './restaurantcard.component.html',
  styleUrls: ['./restaurantcard.component.css']
})
export class RestaurantcardComponent implements OnInit {

  @Input() restaurant;

  constructor() { }

  ngOnInit() {
  }

}
