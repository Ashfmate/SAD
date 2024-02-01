$$
\begin{array}{l}
%% ARGLIST
\text{ARGLIST} \rightarrow 
\text{id ARGTAIL| }\epsilon\\
\text{ARGTAIL} \rightarrow 
\text{, id ARGTAIL | } \epsilon
%% ARGLIST production 
\\ ----------------------------- \\ 
%% BINARYOPERATORS production
\text{BINARYOP1} \rightarrow \text{/ | *}\\
\text{BINARYOP2} \rightarrow \text{+ | -}\\
\text{BINARYOP3} \rightarrow \text{\&\& | ||}\\
\text{BINARYOP4} \rightarrow \text{\& | |}
%% BINARYOPERATORS production
\\ ----------------------------- \\
%% UNARYOPERATORS production
\text{UNARYOP1} \rightarrow \text{++}\\
\text{UNARYOP2} \rightarrow	\text{-}
%% UNARYOPERATORS production
\\ ----------------------------- \\
%% UNARYOPERATIONEXPR production
\text{UNARYOPERATIONEXPR} \rightarrow
\begin{array}{l} \space\space
	\text{UNARYOP1 EXPR}
	\\|\space
	\text{UNARYOP2 EXPR}
	\\|\space
	\text{(EXPR)}
	\\|\space
	\text{id}
	\\|\space
	\text{id(ARGLIST)}
\end{array}
%% UNARYOPERATIONEXPR production
\\ ----------------------------- \\
%% EXPR production
\text{EXPR} \rightarrow
\text{UNARYOPERATIONEXPR EXPR\_REST}\\\\
\text{EXPR\_REST} \rightarrow
\begin{array}{l} \space\space
	\text{BINARYOP1 UNARYOPERATIONEXPR EXPR\_REST}
	\\ |\space
	\text{BINARYOP2 UNARYOPERATIONEXPR EXPR\_REST}
	\\ |\space
	\text{BINARYOP3 UNARYOPERATIONEXPR EXPR\_REST}
	\\ |\space
	\text{BINARYOP4 UNARYOPERATIONEXPR EXPR\_REST}
	\\ |\space\epsilon
\end{array}
%% EXPR production
\\ ----------------------------- \\
%% DATA production
\text{DATA}\rightarrow\text{int | char | float}
%% DATA production
\\ ----------------------------- \\
%% DATA production
\text{OPTDATA}\rightarrow\text{DATA | }\epsilon
%% DATA production
\\ ----------------------------- \\
%% STMT production
\text{STMT} \rightarrow
\begin{array}{l} \space\space
	\text{id : OPTDATA = EXPR}
	\\|\space
	\text{id : DATA}
\end{array}
%% STMT production
\end{array}
$$