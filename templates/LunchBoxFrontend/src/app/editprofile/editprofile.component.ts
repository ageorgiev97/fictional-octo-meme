import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api-service/api.service';
import { FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-editprofile',
  templateUrl: './editprofile.component.html',
  styleUrls: ['./editprofile.component.css']
})
export class EditprofileComponent implements OnInit {

  dishes
  profile
  form
  dishForm

  constructor(private api: ApiService, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.api.getAllDishesForRestaurant().subscribe(result => {
      this.dishes = result;
    })

    this.api.getProfile().subscribe(result => {
      this.profile = result;
      this.setValues();
    })

    this.form = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      lunch_start: ['', Validators.required],
      lunch_end: ['', Validators.required]
    })

    this.dishForm = this.formBuilder.group({
      name: ['', Validators.required],
      calories: ['', Validators.required],
      cost: ['', Validators.required],
      cost_currency: ['', Validators.required],
      grams: ['', Validators.required]
    })

  }

  setValues() {
    this.form
      .patchValue({
        name: this.profile.name,
        description: this.profile.description,
        lunch_start: this.profile.lunch_start,
        lunch_end: this.profile.lunch_end
      })
  }

  setValueToData() {
    this.profile.name = this.form.get('name').value
    this.profile.description = this.form.get('description').value
    this.profile.lunch_start = this.form.get('lunch_start').value
    this.profile.lunch_end = this.form.get('lunch_end').value
  }

  updateProfile() {
    this.setValueToData();
    this.api.updateProfile(this.profile);
  }

  addDish(dish){
    this.api.addDish(dish).subscribe(res => {
      this.ngOnInit();
    });
  }

  deleteDish(dishId){
    this.api.deleteDish(dishId).subscribe(res => {
      this.ngOnInit();
    });
  }
}
