import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http'
import { RouterModule } from '@angular/router'
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { 
  MatButtonModule,
  MatMenuModule,
  MatTabsModule,
  MatButtonToggleModule,
  MatInputModule, 
  MatToolbarModule,
  MatCardModule,
  MatSidenavModule,
  MatIconModule,
  MatFormFieldModule,
  MatSelectModule,
  MatExpansionModule,
  MatSnackBarModule, 
  MatListModule } from '@angular/material';
import { FormsModule, ReactiveFormsModule } from '@angular/forms'
import { LayoutModule } from '@angular/cdk/layout';
import { RegisterComponent } from './registration/register.component'
import { LoginComponent } from './login/login.component'
import { AuthService } from './services/auth-service/auth.service'
import { AuthInterceptor } from './services/auth-service/auth.interceptor'
import { ApiService } from './services/api-service/api.service'

import { AppComponent } from './app.component';
import { FooterComponent } from './footer/footer.component';
import { MenuComponent } from './menu/menu.component';

const routes = [
  { path: '', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent }
]

@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent,
    LoginComponent,
    FooterComponent,
    MenuComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatTabsModule,
    MatButtonToggleModule,
    MatSnackBarModule,
    MatInputModule,
    MatSelectModule,
    MatExpansionModule,
    RouterModule.forRoot(routes),
    MatCardModule,
    LayoutModule,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatToolbarModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    MatMenuModule
  ],
  providers: [AuthService, ApiService, {
    provide: HTTP_INTERCEPTORS,
    useClass: AuthInterceptor,
    multi: true
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
