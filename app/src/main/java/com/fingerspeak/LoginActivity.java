package com.fingerspeak;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckedTextView;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.res.ResourcesCompat;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import www.sanju.motiontoast.MotionToast;
import www.sanju.motiontoast.MotionToastStyle;


public class LoginActivity extends AppCompatActivity {


    //Inicializamos los componentes
    private EditText editTextUsername;
    private EditText editTextPassword;
    private Button btnLogin;
    private CheckedTextView createAccut;

    private CheckedTextView forgotPassword;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_login);


        getComponents(); //Método para obtener los componentes
        linkEvents(); //Método para ligar eventos a los componentes

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.login), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }

    private void getComponents(){

        btnLogin = findViewById(R.id.btnLogin); //Obtenemos el boton de login
        editTextUsername = findViewById(R.id.userName); //Obtenemos el campo de Username
        editTextPassword = findViewById(R.id.password); //Obtenemos el campo de Password
        createAccut = findViewById(R.id.checkCreate); //Obtenemos el campo de crear Cuenta
        forgotPassword = findViewById(R.id.checkForgot); //Obtenemos el campo de reinicio de contraseña




        hideComponents();
    }

    private void hideComponents(){
        //Ocultamos inicialmente la etiqueta de reiniciar contraseña
        forgotPassword.setVisibility(View.INVISIBLE);

    }

    private void linkEvents(){
        // Configurar un escuchador de clics para el botón de inicio de sesión
        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Llamar al método validateLogin cuando se hace clic en el botón
                validateLogin();
            }
        });

        createAccut.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                createAccut();
            }
        });

        forgotPassword.setOnClickListener(new  View.OnClickListener() {

            @Override
            public void onClick(View w){
                resetPassword();
            }
        });

    }


    private void setMessageWaring(String menssage){
        MotionToast.Companion.darkToast(LoginActivity.this,
                "Advertencia",
                menssage,
                MotionToastStyle.WARNING,
                MotionToast.GRAVITY_BOTTOM,
                MotionToast.LONG_DURATION,
                ResourcesCompat.getFont(LoginActivity.this, www.sanju.motiontoast.R.font.helveticabold));

    }

    private void setMenssageError(String menssage){
        MotionToast.Companion.darkToast(LoginActivity.this,
                "Error",
                menssage,
                MotionToastStyle.ERROR,
                MotionToast.GRAVITY_BOTTOM,
                MotionToast.LONG_DURATION,
                ResourcesCompat.getFont(LoginActivity.this, www.sanju.motiontoast.R.font.helveticabold));
    }


    private void validateLogin(){
        String username = editTextUsername.getText().toString();
        String password = editTextPassword.getText().toString();

        if(!username.isEmpty() && !password.isEmpty()){
            setMenssageError("No se pudo establecer la conexión, intentélo más tarde");



       }else{
            if (username.isEmpty()) {
               setMessageWaring("Porfavor ingrese su usuario");

            } else if (password.isEmpty()) {
                setMessageWaring("Porfavor ingrese su contraseña");
            }
        }
    }

    private void createAccut(){
        setMessageWaring("Opción aún no disponible");
    }

    private void resetPassword(){
        setMessageWaring("Opción aún no disponible");
    }



}//Fin de la clase